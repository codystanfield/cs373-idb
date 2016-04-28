'use strict';

angular.module('mixopediaApp', [
    'ngRoute',
    'ngSanitize',
    'mixopediaApp.home',
    'mixopediaApp.cocktails',
    'mixopediaApp.ingredients',
    'angularUtils.directives.dirPagination',
    'mixopediaApp.about',
    'mixopediaApp.search',
    'mixopediaApp.beers'
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
            controller: 'aboutCtrl',
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
        .when('/search/:query', {
          templateUrl:'/static/partials/search.html',
          controller: "searchCtrl",
          controllerAs: 'search',
          activeTab: ""
        })
        .when('/beers', {
          templateUrl:'/static/partials/beers.html',
          controller: "beersCtrl",
          controllerAs: 'beers',
          activeTab: ""
        })
        .otherwise({redirectTo: '/'});

}])

.controller('indexCtrl', ['$scope', '$route', '$location', function($scope, $route, $location){
    $scope.$route = $route;

}]);
