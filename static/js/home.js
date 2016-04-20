angular.module('mixopediaApp.home', ['ngRoute'])

.controller('homeCtrl', ['$scope', function($scope){
    $scope.selectedDay;
    $scope.selectedMonth;
    $scope.selectedYear;
    $scope.age;

    $scope.days = [{
        id: 1,
        date: 3
    }, {
        id: 2,
        date: 15
    }, {
        id: 3,
        date: 30
    }];

    $scope.months = [{
        id: 1,
        date: 8
    }, {
        id: 2,
        date: 9
    }, {
        id: 3,
        date: 10
    }];

    $scope.years = [{
        id: 1,
        date: 1960
    }, {
        id: 2,
        date: 1963
    }, {
        id: 3,
        date: 1980
    }];

    $scope.dateDiff = function (birthMonth, birthDay, birthYear) {
        var todayDate = new Date(),
            todayYear = todayDate.getFullYear(),
            todayMonth = todayDate.getMonth(),
            todayDay = todayDate.getDate(),
            age = todayYear - birthYear.date;

        if (todayMonth < birthMonth.date - 1) {
            age--;
        }

        if (birthMonth.date - 1 === todayMonth && todayDay < birthDay.date) {
            age--;
        }

        return $scope.age = age;
    };

}]);