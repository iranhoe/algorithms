(function () {
    var insertionSort = function (A) {
        for (var j = 0; j < A.length; j++) {
            var key = A[j];
            var i = j - 1;
            while (i > -1 && A[i] > key) {
                A[i + 1] = A[i];
                i = i - 1;
            }
            A[i + 1] = key;
        }
    };
    var elements = [5, 2, 4, 6, 1, 3];
    insertionSort(elements);
    console.log(elements);
})();
