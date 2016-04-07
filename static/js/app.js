'use strict';

angular.module('mixopediaApp', [
    'ngRoute',
    'ngSanitize',
    'mixopediaApp.home',
    'mixopediaApp.cocktails',
    'mixopediaApp.ingredients',
    'angularUtils.directives.dirPagination'
])

.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
    $locationProvider.html5Mode(true);

    $routeProvider
        .when('/', {
            templateUrl: '/static/partials/home.html',
            controller: 'homeCtrl',
            controllerAs: 'home',
            activeTab: ''
        })
        .when('/about', {
            templateUrl: '/static/partials/about.html',
            controller: '',
            controllerAs: 'about',
            activeTab: 'About'
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

}])

.controller('indexCtrl', ['$scope', '$route', '$location', function($scope, $route, $location){
    $scope.$route = $route;

}]);
