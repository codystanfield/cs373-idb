'use strict';

angular.module('mixopediaApp.cocktails', ['ngRoute'])


.controller('cocktailsCtrl', ['$scope', '$filter', '$location', 'drinkRepository', function($scope, $filter, $location, drinkRepository){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  // $scope.letterLimit  = 100;
  // $scope.search   = '';     // set the default search/filter term

  //$location.path('cocktails.html')
  $scope.drinks = drinkRepository.getAllDrinks();

  $scope.goToCocktail = function(cur_id){
    console.log(cur_id.cocktail);
    var cocktail = $filter('filter')($scope.drinks, {id: cur_id.cocktail});
    $location.path('/cocktails/' + cur_id.cocktail);
    //console.log('/cocktail/' + cur_id.cocktail );
  };

}])
.controller('cocktailCtrl', ['$scope', '$routeParams', 'drinkRepository', function($scope, $routeParams, drinkRepository){
  console.log("in cocktail.js");
  console.log($routeParams.cocktailID);
  $scope.whichCocktail = $routeParams.cocktailID;

  // $scope.weird = drinkRepository.getAllDrinks();

  // $scope.name = $scope.drinks[indexOfCocktail].name;
  // console.log($scope.drinks);
  // $scope.drink = $scope.drinks[indexOfCocktail];

  // // $scope.drinks = drinkRepository.getAllDrinks();
  // console.log($scope.drink);

  $scope.drinks = drinkRepository.getAllDrinks();
  $scope.drink = $scope.drinks[$routeParams.cocktailID];
  
  // console.log($scope.drinks[$routeParams.cocktailID].name);
}])
.factory('drinkRepository', function() {
  return {
    getAllDrinks: function (){
      return [
        //Name, glass, image, ingredients, recipe
        {id: 0, name: 'Moscow Mule', ingredients: ["vodka", "mint", "lime juice", "ginger beer"], glass: 'Copper Mug', image: '/static/images/cocktails/Moscow-Mule.png', recipe: "Squeeze lime juice into a Collins glass (or Moscow Mule mug) and drop in the spent shell. Add 2 or 3 ice cubes, then pour in the vodka and fill with cold ginger beer (not ginger ale, although what the hell). Serve with a stirring rod. The Moscow Mule is not, by the way, the first silly vodka drink. That distinction belongs to the Blue Monday, first printed in the English Savoy bar book in 1930. The BM, which appears to have been quite popular in Europe, mixes vodka with a splash of Cointreau, which is just a superior brand of triple sec or white curaçao, and blue food coloring. It's a simple step to premix the curaçao and the dye, yielding blue curaçao -- the first artificial liqueur (have you ever seen a blue-orange?)."},
        {id: 1, name: 'White Russian', ingredients: ["vodka", "kahlua", "heavy cream"], glass: 'old-fashioned', image: '/static/images/cocktails/white-russian.jpg', recipe: "Shake well with cracked ice, then strain into a chilled Old-Fashioned glass (it'll look less wicked than in a martini glass; that's important). Some folks build this one on the rocks, floating the cream on top. No."},
        {id: 2, name: 'Mojito', ingredients: ["lime juice", "sugar", "mint" , "rum", "club soda"], glass: "old-fashioned", image: '/static/images/cocktails/mojito.jpg', recipe: "In a smallish Collins glass, muddle lime juice with 1/2 to 1 teaspoon superfine sugar.* Add the few mint leaves, mushing them against the side of the glass. Fill glass 2/3 with cracked ice and pour in the rum.** Pitch in the squeezed-out lime shell and top off with club soda or seltzer. Serve with a stirring rod. This one responds well to playing around, as long as you keep it within limits. There are some who like to replace the sugar with 2 teaspoons cane syrup; it's hard to find here, but you can make a pretty good substitute by bringing a cup of Demerara sugar (\"Sugar in the Raw\" works) to a gentle boil with 1/2 cup water; keep refrigerated. In either case, it adds a nice mellowness to the thing. Some -- cocktail historian and restaurant critic William Grimes, for one -- prefer their mojitos to be Draques, sin fizz. That's good, too. We like ours with the fizz, though, but also with a tablespoon of 151-proof Demerara rum floated on top. Another wrinkle has to do with the mint. The Cuban species, \"yerba buena,\" is different from the standard U.S. spearmint; supposedly, the Cuban stuff is available. Worth keeping an eye out for." }
      ];
    }
  };
});

