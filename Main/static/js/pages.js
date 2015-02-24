(function(){
    var app = angular.module('echo-directives', []);

    app.directive("productNavBar", function() {
      return {
        restrict: 'E',
        templateUrl: "Nav-Bar.html"
      };
    });
})();

