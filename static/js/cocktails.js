angular.module('mixopediaApp.cocktails', ['ngRoute'])

.controller('cocktailsCtrl', ['$scope', function($scope){
    //$location.path('cocktails.html')
    $scope.drinks = [
      {name: 'drink1'},
      {name: 'drink2'}
    ];

    console.log($scope.drinks);
}]);