'use strict';

angular.module('mixopediaApp.search', ['ngRoute'])


.controller('searchCtrl', ['$scope', '$routeParams', '$filter', '$location', '$http', function($scope, $routeParams, $filter, $location, $http){

  $scope.search = function(query) {
    $location.path('/search/' + query);
  };

  $scope.query = $routeParams.query;

  

  // $http({
  //   method: 'GET',
  //   url: '/api/cocktail'
  // }).then(function successCallback(response) {
  //   // this callback will be called asynchronously
  //   // when the response is available
  //   angular.forEach(response.data, function(key){
  //     var cur_id = key["id"];
  //     $http({
  //       method: 'GET',
  //       url: '/api/cocktail/' + cur_id
  //     }).then(function successCallback(response) {
  //       angular.forEach(response.data, function(drink){
  //         $scope.drinks.push(drink);
  //       });
  //     }, function errorCallback(response) {
  //       // called asynchronously if an error occurs
  //       // or server returns response with an error status.
  //       console.log(response);
  //     });
  //   });
  // }, function errorCallback(response) {
  //   // called asynchronously if an error occurs
  //   // or server returns response with an error status.
  //   console.log(response);
  // });
  //
  // $scope.goToCocktail = function(cur_id){
  //   $location.path('/cocktails/' + cur_id.cocktail);
  // };

}]);
