'use strict';

angular.module('mixopediaApp.cocktails', ['ngRoute', 'ngResource'])


.controller('cocktailsCtrl', ['$scope', '$filter', '$location', '$resource', '$http', 'drinkRepository', function($scope, $filter, $location, $resource, $http, drinkRepository){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order

  // $scope.drinks = drinkRepository.getAllDrinks();


  var CocktailAPI = $resource("http://www.thecocktaildb.com/api/json/v1/1/filter.php",
    { callback: "JSON_CALLBACK" },
    { get: { method: "JSONP" }});

  $scope.getAllCocktails = function() {
    var cocktails = CocktailAPI.get({ c:  "Cocktail"});
    // .$promise.then(function(data) {
    //   $scope.temp  = data.toJSON();
    // }); 

    $scope.temp = JSON.parse(angular.toJson(cocktails));
    // cocktails.$resolved.
    angular.forEach(cocktails, function(key, value) {
       $scope.drinks = value;
    });
    //$scope.drinks = cocktails.drinks.strDrink;
    //scope.user = User.get( {username: 'bob'}  );    // GET
    // cocktails.$promise.then(function(data) {
    //   $scope.drinks = data;
    // });

    // $scope.temp = cocktails;

    
    // angular.forEach(cocktails, function(key, value){
    //   $scope.drinks = value;
    // });

  };

  // $scope.getAllCocktails = function () {
  //   $http({method : 'jsonp', url : 'http://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail'})
  //           .success(function(data, status) {
  //               $scope.drinks = data.toJSON();
  //           })
  //           .error(function(data, status) {
  //               alert(status);
  //           });
  // };

  $scope.goToCocktail = function(cur_id){
    $location.path('/cocktails/' + cur_id.cocktail);
  };

}])
.controller('cocktailCtrl', ['$scope', '$routeParams', '$location', 'drinkRepository', function($scope, $routeParams, $location, drinkRepository){
  $scope.drinks = drinkRepository.getAllDrinks();
  $scope.drink = $scope.drinks[$routeParams.cocktailID];

  $scope.goToIngredient = function(item) {  
    if(item.ingredientName == 'vodka'){
      $location.path('/ingredients/' + 0);
    } else if(item.ingredientName == 'club soda'){
      $location.path('/ingredients/' + 1);
    } else if(item.ingredientName == 'mint'){
      $location.path('/ingredients/' + 2);
    } else if(item.ingredientName == 'ginger beer'){
      $location.path('/ingredients/' + 3);
    } else if(item.ingredientName == 'lime juice'){
      $location.path('/ingredients/' + 4);
    } else if(item.ingredientName == 'heavy cream'){
      $location.path('/ingredients/' + 5);
    } else if(item.ingredientName == 'kahlua'){
      $location.path('/ingredients/' + 6);
    } else if(item.ingredientName == 'rum'){
      $location.path('/ingredients/' + 7);
    } else {
      $location.path('/ingredients/' + 8);
    }
  };
  
}])
.factory('drinkRepository', function() {
  return {
    getAllDrinks: function (){
      return [
        {id: 0, name: 'Moscow Mule', ingredients: ["vodka", "mint", "lime juice", "ginger beer"], glass: 'Copper Mug', image: '/static/images/cocktails/Moscow-Mule.png', recipe: "Squeeze lime juice into a Collins glass (or Moscow Mule mug) and drop in the spent shell. Add 2 or 3 ice cubes, then pour in the vodka and fill with cold ginger beer (not ginger ale, although what the hell). Serve with a stirring rod. The Moscow Mule is not, by the way, the first silly vodka drink. That distinction belongs to the Blue Monday, first printed in the English Savoy bar book in 1930. The BM, which appears to have been quite popular in Europe, mixes vodka with a splash of Cointreau, which is just a superior brand of triple sec or white curaçao, and blue food coloring. It's a simple step to premix the curaçao and the dye, yielding blue curaçao -- the first artificial liqueur (have you ever seen a blue-orange?)."},
        {id: 1, name: 'White Russian', ingredients: ["vodka", "kahlua", "heavy cream"], glass: 'old-fashioned', image: '/static/images/cocktails/white-russian.jpg', recipe: "Shake well with cracked ice, then strain into a chilled Old-Fashioned glass (it'll look less wicked than in a martini glass; that's important). Some folks build this one on the rocks, floating the cream on top. No."},
        {id: 2, name: 'Mojito', ingredients: ["lime juice", "sugar", "mint" , "rum", "club soda"], glass: "old-fashioned", image: '/static/images/cocktails/mojito.jpg', recipe: "In a smallish Collins glass, muddle lime juice with 1/2 to 1 teaspoon superfine sugar.* Add the few mint leaves, mushing them against the side of the glass. Fill glass 2/3 with cracked ice and pour in the rum.** Pitch in the squeezed-out lime shell and top off with club soda or seltzer. Serve with a stirring rod. This one responds well to playing around, as long as you keep it within limits. There are some who like to replace the sugar with 2 teaspoons cane syrup; it's hard to find here, but you can make a pretty good substitute by bringing a cup of Demerara sugar (\"Sugar in the Raw\" works) to a gentle boil with 1/2 cup water; keep refrigerated. In either case, it adds a nice mellowness to the thing. Some -- cocktail historian and restaurant critic William Grimes, for one -- prefer their mojitos to be Draques, sin fizz. That's good, too. We like ours with the fizz, though, but also with a tablespoon of 151-proof Demerara rum floated on top. Another wrinkle has to do with the mint. The Cuban species, \"yerba buena,\" is different from the standard U.S. spearmint; supposedly, the Cuban stuff is available. Worth keeping an eye out for." }
      ];
    }
  };
});

