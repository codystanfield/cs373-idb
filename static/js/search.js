'use strict';

angular.module('mixopediaApp.search', ['ngRoute'])


.controller('searchCtrl', ['$scope', '$routeParams', '$filter', '$location', '$http', '$sce', function($scope, $routeParams, $filter, $location, $http, $sce){

  $scope.search = function(query) {
    $location.path('/search/' + query);
  };

  $scope.query = $routeParams.query;

  $scope.drinks_and = [];
  $scope.items_and = [];

  $scope.drinks_or = [];
  $scope.items_or = [];

  $scope.highlight = function(text, search) {
    if (!search) {
      console.log("NO SEARCH")
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
    // this callback will be called asynchronously
    // when the response is available
    //console.log(response.data);
    console.log(response.data);

    angular.forEach(response.data, function(key, value){
      var category = value;
      console.log(value);
      angular.forEach(key, function(list, boolean) {
        console.log(boolean);
        var and_or = boolean;
        // iterate through the list of items
        angular.forEach(list, function(item_id) {
          console.log(item_id);
          console.log('/api/' + category + '/' + item_id);
          var temp = '/api/' + category + '/' + item_id;
          $http({
            method: 'GET',
            url: temp
          }).then(function successCallback(response) {
            console.log("**** response " + response.data);
            angular.forEach(response.data, function(drink_or_ingredient){
              if(and_or == "and" && category == "cocktail"){
                $scope.drinks_and.push(drink_or_ingredient);
              } else if(and_or == "or" && category == "cocktail"){
                $scope.drinks_or.push(drink_or_ingredient);
              } else if(and_or == "and" && category == "ingredient") {
                $scope.items_and.push(drink_or_ingredient);
              } else if(and_or == "or" && category == "ingredient") {
                $scope.items_or.push(drink_or_ingredient);
              }
            });
          }, function errorCallback(response) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            console.log(response);
          });
        });
      });
      console.log(key + " value: " + value);

      console.log(value + " " + key.and);
      console.log(value + " " + key.or);

      // angular.forEach(key.and, )
      // console.log(cocktails);
      //var cur_id = cocktails;
      // $http({
      //   method: 'GET',
      //   url: '/api/cocktail/' + cur_id
      // }).then(function successCallback(response) {
      //   angular.forEach(response.data, function(drink){
      //     $scope.drinks.push(drink);
      //   });
      // }, function errorCallback(response) {
      //   // called asynchronously if an error occurs
      //   // or server returns response with an error status.
      //   console.log(response);
      // });
    });

    $scope.goToCocktail = function(cur_id){
      $location.path('/cocktails/' + cur_id.cocktail);
    };
    $scope.goToIngredient = function(cur_id){
      // var ingredient = $filter('filter')($scope.ingredients, {id: cur_id.ingredientID});
      $location.path('/ingredients/' + cur_id.itemID);
    };
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });
  //
  // $scope.goToCocktail = function(cur_id){
  //   $location.path('/cocktails/' + cur_id.cocktail);
  // };

  // $scope.highlight = function(haystack, needle) {
  //   if(!needle) {
  //     return $sce.trustAsHtml(haystack);
  //   }
  //   return $sce.trustAsHtml(haystack.replace(new RegExp(needle, "gi"), function(match) {
  //     return '<span class="highlightedText">' + match + '</span>';
  //   }));
  // };

}]);
