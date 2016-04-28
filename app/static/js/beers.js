'use strict';

angular.module('mixopediaApp.beers', ['ngRoute'])

.controller('beersCtrl', ['$scope', '$filter', '$location', '$http', function($scope, $filter, $location, $http){

  $scope.beers = [];
  $http({
    method: 'GET',
    url: '/api/beer'
  }).then(function successCallback(response) {
    console.log(response);
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });


}]);
