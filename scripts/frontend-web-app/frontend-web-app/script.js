document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var searchTerm = document.getElementById('searchTerm').value;
    fetch('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=' + encodeURIComponent(searchTerm) + '&origin=*')
        .then(function(response) {
            return response.json();
        })
        .then(function(results) {
            var resultList = document.getElementById('results');
            resultList.innerHTML = '';
            for (var i = 0; i < results[1].length; i++) {
                var listItem = document.createElement('li');
                var link = document.createElement('a');
                link.href = results[3][i];
                link.textContent = results[1][i];
                listItem.appendChild(link);
                resultList.appendChild(listItem);
            }
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
});