'use strict';

angular.module('mixopediaApp.cocktails', ['ngRoute'])


.controller('cocktailsCtrl', ['$scope', '$filter', '$location', '$http', function($scope, $filter, $location, $http){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order

  $scope.drinks = [];
  $http({
    method: 'GET',
    url: '/api/cocktail'
  }).then(function successCallback(response) {
    // this callback will be called asynchronously
    // when the response is available
    angular.forEach(response.data, function(key){
      var cur_id = key["id"];
      $http({
        method: 'GET',
        url: '/api/cocktail/' + cur_id
      }).then(function successCallback(response) {
        angular.forEach(response.data, function(drink){
          $scope.drinks.push(drink);
        });
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        console.log(response);
      });
    });
    console.log($scope.drinks);
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });

  $scope.goToCocktail = function(cur_id){
    $location.path('/cocktails/' + cur_id.cocktail);
  };

}])
.controller('cocktailCtrl', ['$scope', '$routeParams', '$location', '$http', function($scope, $routeParams, $location, $http){
  $scope.drink = [];
  $http({
    method: 'GET',
    url: '/api/cocktail/' + $routeParams.cocktailID
  }).then(function successCallback(response) {
    $scope.drink = response.data[0];
    console.log(response.data[0]);
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });

  $scope.goToIngredient = function(i) {  
    $location.path('/ingredients/' + i.ingredientID);
  };
  
}]);

