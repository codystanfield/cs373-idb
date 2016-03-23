'use strict';

angular.module('mixopediaApp', [
    'ngRoute',
    'ngSanitize',
    'mixopediaApp.home',
    'mixopediaApp.cocktails',
    'mixopediaApp.ingredients',
])

.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){

    $locationProvider.html5Mode(true);
    // $locationProvider.hashPrefix('!');

    $routeProvider
        .when('/', {
            templateUrl: '/static/partials/home.html',
            controller: 'homeCtrl',
            controllerAs: 'home',
            activeTab: ''
        })
        .when('/cocktails', {
            templateUrl: '/static/partials/cocktails.html',
            controller: 'cocktailsCtrl',
            controllerAs: 'cocktails',
            activeTab: 'Cocktails'
        })
        .when('/cocktails/:cocktailID', {
            templateUrl: '/static/partials/cocktail.html',
            controller: "cocktailCtrl",
            controllerAs: 'cocktail',
            activeTab: ""
        })
        .when('/ingredients', {
            templateUrl: '/static/partials/ingredients.html',
            controller: 'ingredientsCtrl',
            controllerAs: 'ingredients',
            activeTab: 'Ingredients'
        })
        .when('/ingredients/:ingredientID', {
            templateUrl: '/static/partials/ingredient.html',
            controller: "ingredientCtrl",
            controllerAs: 'ingredient',
            activeTab: ""
        })
        .otherwise({redirectTo: '/'});
        
    //$locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', '$location', function($scope, $route, $location){
    $scope.$route = $route;

    // $scope.range = function(n){
    //     var ans = [];
    //     for(var i = 0; i < n; i += 1){
    //         ans.push(i);
    //     }
    //     return ans;
    // };
    // $scope.submitQuery = function(){
    //     $location.path("/search/" + $scope.query); // path not hash
    // };

}]);