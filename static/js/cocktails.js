angular.module('mixopediaApp.cocktails', ['ngRoute'])

.controller('cocktailsCtrl', ['$scope', function($scope){
    //$location.path('cocktails.html')
    $scope.drinks = [
      {name: 'Moscow Mule', img: '/static/images/cocktails/Moscow-Mule.png'},
      {name: 'White Russian', img: '/static/images/cocktails/white-russian.jpg'},
      {name: 'Mojito'}
    ];

    console.log($scope.drinks);
}]);