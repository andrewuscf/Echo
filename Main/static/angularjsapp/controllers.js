//angular.module('echoApp.controllers',[]).controller('UserListController',function($scope,$state,popupService,$window,User){
//    $scope.users = User.query(); //go get all the data
//
//    $scope.deleteUser = function(user){
//        if (popupService.showPopup('Really delete this?')){
//            user.$delete(function(){
//               $window.location.href = '' ;//go home
//            });
//        }
//    }
//}).controller('UserViewController',function($scope,$stateParams, User){
//    $scope.user = User.get({id: $stateParams.id }); // Get a single echo
//}).controller('UserCreateController', function($scope, $state, $stateParams, User){
//    $scope.user = new User();
//
//    $scope.addUser = function(){
//      $scope.user.$save(function(){
//        $state.go('users'); //go back home
//      });
//    }
//}).controller('UserEditController',function($scope, $state, $stateParams, User){
//    $scope.updateUser = function(){
//      $scope.user.$update(function(){
//        $state.go('users');
//      });
//    };
//    $scope.loadUser = function(){
//      $scope.user = User.get({id: $stateParams.id });
//    };
//   $scope.loadUser();
//});