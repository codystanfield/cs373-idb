'use strict';

angular.module('mixopediaApp.search', ['ngRoute'])


.controller('searchCtrl', ['$scope', '$routeParams', '$filter', '$location', '$http', '$sce', function($scope, $routeParams, $filter, $location, $http, $sce){

  $scope.search = function(query) {
    $location.path('/search/' + query);
  };

  $scope.query = $routeParams.query;

  $scope.countOfQuery = function() {
    var text = $scope.query;
    var s = text ? text.split(/\s+/) : 0; // it splits the text on space/tab/enter
    return s ? s.length : '';
  };

  $scope.numWordsInQuery = $scope.countOfQuery();

  $scope.drinks_and = [];
  $scope.items_and = [];

  $scope.drinks_or = [];
  $scope.items_or = [];

  $scope.highlight = function(text, search) {
    if (!search) {
      return $sce.trustAsHtml(text);
    }
    return $sce.trustAsHtml(text.toString().replace(new RegExp(search.toString(), 'gi'), '<span class="highlightedText">$&</span>'));
  };

  $http({
    method: 'GET',
    url: '/api/query',
    headers: {
      "query": $scope.query
    }
  }).then(function successCallback(response) {
    // iteratate through each ingredients or cocktails array
    angular.forEach(response.data, function(key, value){
      // set the category to ingredients or cocktails
      var category = value;

      // there are two lists OR and AND
      angular.forEach(key, function(list, boolean) {
        // set the boolean
        var and_or = boolean;
        // iterate through the list of items
        angular.forEach(list, function(item_id) {

          var apiUrl = '/api/' + category + '/' + item_id;
          $http({
            method: 'GET',
            url: apiUrl
          }).then(function successCallback(response) {
            // iterate through cocktail or ingredient and add items to the list
            angular.forEach(response.data, function(drink_or_ingredient){
              // only create 1 array for drinks and 1 for ingredients if it
              // is a single word query
              if($scope.numWordsInQuery == 1){
                if(and_or == "and" && category == "cocktail"){
                  $scope.drinks_and.push(drink_or_ingredient);
                } else if(and_or == "and" && category == "ingredient") {
                  $scope.items_and.push(drink_or_ingredient);
                }
              } else {
                if(and_or == "and" && category == "cocktail"){
                  $scope.drinks_and.push(drink_or_ingredient);
                } else if(and_or == "or" && category == "cocktail"){
                  $scope.drinks_or.push(drink_or_ingredient);
                } else if(and_or == "and" && category == "ingredient") {
                  $scope.items_and.push(drink_or_ingredient);
                } else if(and_or == "or" && category == "ingredient") {
                  $scope.items_or.push(drink_or_ingredient);
                }
              }
            });
          }, function errorCallback(response) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            console.log(response);
          });
        });
      });
    });

    $scope.goToCocktail = function(cur_id){
      $location.path('/cocktails/' + cur_id.cocktail);
    };

    $scope.goToIngredient = function(cur_id){
      $location.path('/ingredients/' + cur_id.itemID);
    };
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });

}]);
