angular.module('mixopediaApp.cocktails', ['ngRoute'])

.controller('cocktailsCtrl', ['$scope', function($scope){

  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  $scope.letterLimit  = 100;
  // $scope.search   = '';     // set the default search/filter term

  //$location.path('cocktails.html')
  $scope.drinks = [

  //Name, glass, image, ingredients, recipe
    {name: 'Moscow Mule', ingredients: ["vodka", "mint", "lime juice", "ginger beer"], glass: 'Copper Mug', image: '/static/images/cocktails/Moscow-Mule.png', recipe: "Squeeze lime juice into a Collins glass (or Moscow Mule mug) and drop in the spent shell. Add 2 or 3 ice cubes, then pour in the vodka and fill with cold ginger beer (not ginger ale, although what the hell). Serve with a stirring rod. The Moscow Mule is not, by the way, the first silly vodka drink. That distinction belongs to the Blue Monday, first printed in the English Savoy bar book in 1930. The BM, which appears to have been quite popular in Europe, mixes vodka with a splash of Cointreau, which is just a superior brand of triple sec or white curaçao, and blue food coloring. It's a simple step to premix the curaçao and the dye, yielding blue curaçao -- the first artificial liqueur (have you ever seen a blue-orange?)."},
    {name: 'White Russian', image: '/static/images/cocktails/white-russian.jpg'},
    {name: 'Mojito', image: '/static/images/cocktails/mojito.jpg' }
  ];

}]);