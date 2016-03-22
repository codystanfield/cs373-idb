angular.module('mixopediaApp.cocktail', ['ngRoute'])

.controller('cocktailCtrl', ['$scope', '$routeParams', function($scope, $routeParams){
  console.log("in cocktail.js");
  $scope.whichCocktail = $routeParams.cocktailID;
}]);

