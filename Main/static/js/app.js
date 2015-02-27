 var echoApp = angular.module('echoApp', ['ngRoute', 'ngResource', 'ngCookies', 'audioPlayer-directive']);

echoApp.config(['$httpProvider', function($httpProvider){
        // django and angular both support csrf tokens. This tells
        // angular which cookie to add to what header.
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]).
    factory('api', function($resource){
        function add_auth_header(data, headersGetter){
            // as per HTTP authentication spec [1], credentials must be
            // encoded in base64. Lets use window.btoa [2]
            var headers = headersGetter();
            headers['Authorization'] = ('Basic ' + btoa(data.username +
                                        ':' + data.password));
        }
        // defining the endpoints. Note we escape url trailing dashes: Angular
        // strips unescaped trailing slashes. Problem as Django redirects urls
        // not ending in slashes to url that ends in slash for SEO reasons, unless
        // we tell Django not to [3]. This is a problem as the POST data cannot
        // be sent with the redirect. So we want Angular to not strip the slashes!
        return {
            auth: $resource('/api/auth\\/', {}, {
                login: {method: 'POST', transformRequest: add_auth_header},
                logout: {method: 'DELETE'}
            }),
            users: $resource('/api/user\\/', {}, {
                create: {method: 'POST'}
            })
        };
    }).
     controller('authController', function($scope, api, $location, $rootScope) {
        // Angular does not detect auto-fill or auto-complete. If the browser
        // autofills "username", Angular will be unaware of this and think
        // the $scope.username is blank. To workaround this we use the
        // autofill-event polyfill [4][5]
        //$('#id_auth_form input').checkAndTriggerAutoFillEvent();

        $scope.getCredentials = function(){
            return {username: $scope.username, password: $scope.password};
        };

        $scope.login = function(){
            api.auth.login($scope.getCredentials()).
                $promise.
                    then(function(data){
                        // on good username and password
                        $scope.user = data.username;
                        $scope.id = data.id;
                        $location.path('/main');
                        $rootScope.username = $scope.user;
                        $rootScope.id = $scope.id;
                    }).
                    catch(function(data){
                        // on incorrect username and password
                        alert(data.data.detail);
                    });
        };

        $scope.logout = function(){
            api.auth.logout(function(){
                $scope.user = undefined;
                $location.path('/');
            });
        };
        $scope.register = function($event){
            // prevent login form from firing
            $event.preventDefault();
            // create user and immediatly login on success
            api.users.create($scope.getCredentials()).
                $promise.
                    then($scope.login).
                    catch(function(data){
                        alert("Someone has that username already!");
                    });
            };


    });








echoApp.config(['$routeProvider' ,function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/views/base.html',
            controller: 'authController'
        }).
        when('/main', {
            templateUrl: '/static/views/MainPage.html',
            controller: 'EchoAppCtrl'
        });

}]);

 echoApp.controller('EchoAppCtrl',function($scope, $http ) {
     var friendSort = function(data) {
         var userlog = null;
         var friend = null;
         var obj_test = data;

         //console.log(obj_test.results);

     };
     $scope.usernamefinal= $scope.username;
     $scope.idfinal = $scope.id;

     $http.get('api/user/').success(function (data) {
         //$scope.name = $rootScope.user;
         $scope.name1 = data;
         console.log($scope.name1)
     });
     $http.get('api/friend/').success(function (data) {
         $scope.friends = data;
         $scope.friendslist = friendSort(data);
         //console.log($scope.friendslist)
     });

     echoApp.directive('audioPlayer', function($rootScope) {
        return {
            restrict: 'E',
            scope: {},
            controller: function($scope, $element) {
                $scope.audio = new Audio();
                $scope.currentNum = 0;

                // tell others to give me my prev/next track (with audio.set message)
                $scope.next = function(){ $rootScope.$broadcast('audio.next'); };
                $scope.prev = function(){ $rootScope.$broadcast('audio.prev'); };

                // tell audio element to play/pause, you can also use $scope.audio.play() or $scope.audio.pause();
                $scope.playpause = function(){ var a = $scope.audio.paused ? $scope.audio.play() : $scope.audio.pause(); };

                // listen for audio-element events, and broadcast stuff
                $scope.audio.addEventListener('play', function(){ $rootScope.$broadcast('audio.play', this); });
                $scope.audio.addEventListener('pause', function(){ $rootScope.$broadcast('audio.pause', this); });
                $scope.audio.addEventListener('timeupdate', function(){ $rootScope.$broadcast('audio.time', this); });
                $scope.audio.addEventListener('ended', function(){ $rootScope.$broadcast('audio.ended', this); $scope.next(); });

                // set track & play it
                $rootScope.$on('audio.set', function(r, file, info, currentNum, totalNum){
                    var playing = !$scope.audio.paused;
                    $scope.audio.src = file;
                    var a = playing ? $scope.audio.play() : $scope.audio.pause();
                    $scope.info = info;
                    $scope.currentNum = currentNum;
                    $scope.totalNum = totalNum;
                });

                // update display of things - makes time-scrub work
                setInterval(function(){ $scope.$apply(); }, 500);
            }
        };
    });

    echoApp.filter('startFrom', function() {
        return function(input, start) {
            start = +start; //parse to int
            return input.slice(start);
        };
    });

    echoApp.controller('MainCtrl', function ($scope, $http, $rootScope) {
        $scope.currentTrack = 0;
        $scope.pageSize = 5;
        $scope.data=[];

        var updateTrack = function(){
            $rootScope.$broadcast('audio.set', 'mp3/' + $scope.data[$scope.currentTrack].file, $scope.data[$scope.currentTrack], $scope.currentTrack, $scope.data.length);
        };

        $rootScope.$on('audio.next', function(){
            $scope.currentTrack++;
            if ($scope.currentTrack < $scope.data.length){
                updateTrack();
            }else{
                $scope.currentTrack=$scope.data.length-1;
            }
        });

        $rootScope.$on('audio.prev', function(){
            $scope.currentTrack--;
            if ($scope.currentTrack >= 0){
                updateTrack();
            }else{
                $scope.currentTrack = 0;
            }
        });

        $http.get('http://127.0.0.1:8000/api/track/3/')
            .success(function(response){
                $scope.data = response;
                updateTrack();
            });
    });

});

 echoApp.controller('EchoController', function ($scope, $http) { // calling the app controller up to the http

 });

