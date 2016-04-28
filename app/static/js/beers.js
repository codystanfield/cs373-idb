'use strict';

angular.module('mixopediaApp.beers', ['ngRoute'])

.controller('beersCtrl', ['$scope', '$filter', '$location', '$http', function($scope, $filter, $location, $http){

  $scope.beers_list = [];

  $http({
    method: 'GET',
    url: '/api/beer'
  }).then(function successCallback(response) {
    console.log(response.data);
    angular.forEach(response.data, function(all_beers){
      angular.forEach(all_beers, function(b){
        $scope.beers_list.push(b);
      });
    });
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });


}]);
