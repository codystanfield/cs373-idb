angular.module('mixopediaApp.cocktails', ['ngRoute'])

.controller('cocktailsCtrl', [function($scope){
    //$location.path('cocktails.html')
    $scope.drinks = [
      {name: 'drink1'},
      {name: 'drink2'}
    ];
}]);