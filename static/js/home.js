angular.module('mixopediaApp.home', ['ngRoute'])

.controller('homeCtrl', ['$scope', function($scope){
    this.greeting = "konichiwa";

    $scope.selectedDay;
    $scope.selectedMonth;
    $scope.selectedYear;
    $scope.age;

    $scope.days = [
        {id: 1, date: 1}, {id: 2, date: 2}, {id: 3, date: 3}, {id: 4, date: 4},
        {id: 5, date: 5}, {id: 6, date: 6}, {id: 7, date: 7}, {id: 8, date: 8},
        {id: 9, date: 9}, {id: 10, date: 10}, {id: 11, date: 11}, {id: 12, date: 12},
        {id: 13, date: 13}, {id: 14, date: 14}, {id: 15, date: 15}, {id: 16, date: 16},
        {id: 17, date: 17}, {id: 18, date: 18}, {id: 19, date: 19}, {id: 20, date: 20},
        {id: 21, date: 21}, {id: 22, date: 22}, {id: 23, date: 23}, {id: 24, date: 24},
        {id: 25, date: 25}, {id: 26, date: 26}, {id: 27, date: 27}, {id: 28, date: 28},
        {id: 29, date: 29}, {id: 30, date: 30}, {id: 31, date: 31}];

    $scope.months = [
        {id: 1, date: 1}, {id: 2, date: 2}, {id: 3, date: 3}, {id: 4, date: 4},
        {id: 5, date: 5}, {id: 6, date: 6}, {id: 7, date: 7}, {id: 8, date: 8},
        {id: 9, date: 9}, {id: 10, date: 10}, {id: 11, date: 11}, {id: 12, date: 12}];

    $scope.years = [
        {id: 2016, date: 2016}, {id: 2015, date: 2015},
        {id: 2014, date: 2014}, {id: 2013, date: 2013},
        {id: 2012, date: 2012}, {id: 2011, date: 2011},
        {id: 2010, date: 2010},

        {id: 2009, date: 2009}, {id: 2008, date: 2008},
        {id: 2007, date: 2007}, {id: 2006, date: 2006},
        {id: 2005, date: 2005}, {id: 2004, date: 2004},
        {id: 2003, date: 2003}, {id: 2002, date: 2002},
        {id: 2001, date: 2001}, {id: 2000, date: 2000},

        {id: 1999, date: 1999}, {id: 1998, date: 1998},
        {id: 1997, date: 1997}, {id: 1996, date: 1996},
        {id: 1995, date: 1995}, {id: 1994, date: 1994},
        {id: 1993, date: 1993}, {id: 1992, date: 1992},
        {id: 1991, date: 1991}, {id: 1990, date: 1990},

        {id: 1989, date: 1989}, {id: 1988, date: 1988},
        {id: 1987, date: 1987}, {id: 1986, date: 1986},
        {id: 1985, date: 1985}, {id: 1984, date: 1984},
        {id: 1983, date: 1983}, {id: 1982, date: 1982},
        {id: 1981, date: 1981}, {id: 1980, date: 1980},

        {id: 1979, date: 1979}, {id: 1978, date: 1978},
        {id: 1977, date: 1977}, {id: 1976, date: 1976},
        {id: 1975, date: 1975}, {id: 1974, date: 1974},
        {id: 1973, date: 1973}, {id: 1972, date: 1972},
        {id: 1971, date: 1971}, {id: 1970, date: 1970},

        {id: 1969, date: 1969}, {id: 1968, date: 1968},
        {id: 1967, date: 1967}, {id: 1966, date: 1966},
        {id: 1965, date: 1965}, {id: 1964, date: 1964},
        {id: 1963, date: 1963}, {id: 1962, date: 1962},
        {id: 1961, date: 1961}, {id: 1960, date: 1960},

        {id: 1959, date: 1959}, {id: 1958, date: 1958},
        {id: 1957, date: 1957}, {id: 1956, date: 1956},
        {id: 1955, date: 1955}, {id: 1954, date: 1954},
        {id: 1953, date: 1953}, {id: 1952, date: 1952},
        {id: 1951, date: 1951}, {id: 1950, date: 1950},

        {id: 1949, date: 1949}, {id: 1948, date: 1948},
        {id: 1947, date: 1947}, {id: 1946, date: 1946},
        {id: 1945, date: 1945}, {id: 1944, date: 1944},
        {id: 1943, date: 1943}, {id: 1942, date: 1942},
        {id: 1941, date: 1941}, {id: 1940, date: 1940},

        {id: 1939, date: 1939}, {id: 1938, date: 1938},
        {id: 1937, date: 1937}, {id: 1936, date: 1936},
        {id: 1935, date: 1935}, {id: 1934, date: 1934},
        {id: 1933, date: 1933}, {id: 1932, date: 1932},
        {id: 1931, date: 1931}, {id: 1930, date: 1930}];

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