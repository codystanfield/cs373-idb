'use strict';

angular.module('mixopediaApp.ingredients', ['ngRoute'])

.controller('ingredientsCtrl', ['$scope', '$filter', '$location', 'ingredientRepository', '$http', function($scope, $filter, $location, ingredientRepository, $http){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  // $scope.letterLimit  = 100;
  // $scope.search   = '';     // set the default search/filter term

  $scope.items = ingredientRepository.getAllIngredients();

  $scope.items = [];
  $http({
    method: 'GET',
    url: '/api/ingredient'
  }).then(function successCallback(response) {
    // this callback will be called asynchronously
    // when the response is available
    angular.forEach(response.data, function(key){
      var cur_id = key["id"];
      $http({
        method: 'GET',
        url: '/api/ingredient/' + cur_id
      }).then(function successCallback(response) {
        angular.forEach(response.data, function(item){
          $scope.items.push(item);
        });
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        console.log(response);
      });
    });
    console.log($scope.items);
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    console.log(response);
  });

  $scope.goToIngredient = function(cur_id){
    // var ingredient = $filter('filter')($scope.ingredients, {id: cur_id.ingredientID});
    $location.path('/ingredients/' + cur_id.itemID);
  };

}])
.controller('ingredientCtrl', ['$scope', '$routeParams', '$location', 'ingredientRepository', function($scope, $routeParams, $location, ingredientRepository){
  $scope.items = ingredientRepository.getAllIngredients();
  $scope.item = $scope.items[$routeParams.ingredientID];
  
  $scope.goToDrink = function(drink) {
    console.log('/cocktails/' + drink.drinkName);
    if(drink.drinkName == 'Moscow Mule'){
      $location.path('/cocktails/' + 0);
    } else if (drink.drinkName == 'White Russian'){
      $location.path('/cocktails/' + 1);
    } else {
      $location.path('/cocktails/' + 2);
    }
  };

}])
.factory('ingredientRepository', function() {
  return {
    getAllIngredients: function (){
      return [
        //Name, glass, image, ingredients, recipe
        {id: 0, name: 'vodka', alcoholic: true, cocktails: ["Moscow Mule", "White Russian"], numCocktails: 2, image: '/static/images/ingredients/vodka.jpg'},
        {id: 1, name: 'club soda', alcoholic: false, cocktails: ["Mojito"], numCocktails: 1, image: '/static/images/ingredients/club+soda.jpg'}, 
        {id: 2, name: 'mint', alcoholic: false, cocktails: ["Mojito", "Moscow Mule"], numCocktails: 2, image: '/static/images/ingredients/mint.jpg'}, 
        {id: 3, name: 'ginger beer', alcoholic: false, cocktails: ["Moscow Mule"], numCocktails: 1, image: '/static/images/ingredients/Ginger+Beer.jpg'}, 
        {id: 4, name: 'lime juice', alcoholic: false, cocktails: ["Moscow Mule", "Mojito"], numCocktails: 2, image: '/static/images/ingredients/Lime+juice.jpg'}, 
        {id: 5, name: 'heavy cream', alcoholic: false, cocktails: ["White Russian"], numCocktails: 1, image: '/static/images/ingredients/Heavy+cream.jpg'}, 
        {id: 6, name: 'kahlua', alcoholic: true, cocktails: ["White Russian"], numCocktails: 1, image: '/static/images/ingredients/Kahlua.jpg'}, 
        {id: 7, name: 'rum', alcoholic: true, cocktails: ["Mojito"], numCocktails: 1, image: '/static/images/ingredients/Rum.jpg'}, 
        {id: 8, name: 'sugar', alcoholic: false, cocktails: ["Mojito"], numCocktails: 1, image: '/static/images/ingredients/Sugar.jpg'}, 

      ];
    }
  };
});

