//angular.module('echoApp.services',[]).factory('User', function($resource){
//    return $resource('/api/user/:Id',{Id: '@Id'},{
//       'update':{
//           method:'PUT'
//       },
//        query: {method: "GET", isArray: false}
//
//    });
//}).service('popupService',function($window){
//    this.showPopup=function(message){
//        return $window.confirm(message);
//    }
//});