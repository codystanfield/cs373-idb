'use strict';

angular.module('mixopediaApp.ingredients', ['ngRoute'])

.controller('ingredientsCtrl', ['$scope', '$filter', '$location', 'ingredientRepository', function($scope, $filter, $location, ingredientRepository){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  // $scope.letterLimit  = 100;
  // $scope.search   = '';     // set the default search/filter term

  $scope.items = ingredientRepository.getAllIngredients();

  $scope.goToIngredient = function(cur_id){
    // var ingredient = $filter('filter')($scope.ingredients, {id: cur_id.ingredientID});
    $location.path('/ingredients/' + cur_id.ingredientID);
  };

}])
// .controller('ingredientCtrl', ['$scope', '$routeParams', 'ingredientRepository', function($scope, $routeParams, ingredientRepository){
//   $scope.ingredients = ingredientRepository.getAllIngredients();
//   $scope.ingredient = $scope.ingredients[$routeParams.ingredientID];
  
// }])
.factory('ingredientRepository', function() {
  return {
    getAllIngredients: function (){
      return [
        //Name, glass, image, ingredients, recipe
        {id: 0, name: 'vodka', alcoholic: true, cocktails: ["Moscow Mule", "White Russian"], numCocktails: 2, image: '/static/images/ingredients/vodka.jpg'},
        {id: 1, name: 'club soda', alcoholic: false, cocktails: ["Mojito"], numCocktails: 1, image: '/static/images/ingredients/club+soda.jpg'}
      ];
    }
  };
});

