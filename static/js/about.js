'use strict';

angular.module('mixopediaApp.about', ['ngRoute'])


.controller('aboutCtrl', ['$scope', '$filter', '$location', '$http', function($scope, $filter, $location, $http){

  $scope.tests = "";
  $scope.getTests = function (){
    $http({
      method: 'GET',
      url: '/tests'
    }).then(function successCallback(response) {
      // this callback will be called asynchronously
      // when the response is available
      $scope.tests = response.data;
      console.log(response.data);
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
      console.log(response);
    });
  };


}]);
