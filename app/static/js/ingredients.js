'use strict';

angular.module('mixopediaApp.ingredients', ['ngRoute'])

.controller('ingredientsCtrl', ['$scope', '$filter', '$location', '$http', function($scope, $filter, $location, $http){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  // $scope.letterLimit  = 100;
  // $scope.search   = '';     // set the default search/filter term

  $scope.items = [];
  $http({
    method: 'GET',
    url: '/api/ingredient'
  }).then(function successCallback(response) {
    // this callback will be called asynchronously
    // when the response is available
    angular.forEach(response.data, function(key){
      var cur_id = key["id"];
      $http({
        method: 'GET',
        url: '/api/ingredient/' + cur_id
      }).then(function successCallback(response) {
        angular.forEach(response.data, function(item){
          $scope.items.push(item);
        });
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        console.log(response);
      });
    });
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });

  $scope.goToIngredient = function(cur_id){
    // var ingredient = $filter('filter')($scope.ingredients, {id: cur_id.ingredientID});
    $location.path('/ingredients/' + cur_id.itemID);
  };

}])
.controller('ingredientCtrl', ['$scope', '$routeParams', '$location', '$http', function($scope, $routeParams, $location, $http){

  $scope.item = [];
  $http({
    method: 'GET',
    url: '/api/ingredient/' + $routeParams.ingredientID
  }).then(function successCallback(response) {
    $scope.item = response.data[0];
    console.log(response.data[0]);
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });

  $scope.goToDrink = function(d) {
    $location.path('/cocktails/' + d.drinkID);
  };

}]);
