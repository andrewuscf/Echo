//var echoApp =angular.module('echoApp',['ngRoute','echoApp.controllers','echoApp.services']);
//
//$http.get('api/user/').success(function(data){
//    $scope.users = data;
//});
//
//
//
//
//echo.config(['$routeProvider',function($routeProvider){
//    $routeProvider.
//        when('/',{
//            templateUrl: 'static/index.html',
//            controller: 'homeController'
//        })
//}]);






//angular.module('echoApp').config(function($stateProvider,$httpProvider){
//    $stateProvider.state('users',{
//        url: '/users',
//        templateUrl: '/templates/users.html',
//        controller:'UserListController',
//        controllerAs: 'userCtrl'
//    }).state('viewUser',{ // a single thing
//        url: '/users/:id/view',
//        templateUrl: 'test.html',
//        controller: 'UserViewController'
//    }).state('newUser',{
//        url: '/users/new',
//        templateUrl: 'test.html',
//        controller: 'UserCreateController'
//    }).state('editUser',{
//        url: '/users/:id/edit',
//        templateUrl: 'test.html',
//        controller: 'UserEditController'
//    });
//}).run(function($state){
//   $state.go('users');
//});
