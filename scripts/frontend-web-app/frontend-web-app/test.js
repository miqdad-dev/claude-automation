var assert = require('assert');

describe('Wikipedia Search', function() {
    it('should return results for a valid search term', function(done) {
        fetch('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=programming&origin=*')
            .then(function(response) {
                return response.json();
            })
            .then(function(results) {
                assert(results[1].length > 0);
                done();
            })
            .catch(done);
    });

    it('should return no results for an invalid search term', function(done) {
        fetch('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=asdfasdfasdf&origin=*')
            .then(function(response) {
                return response.json();
            })
            .then(function(results) {
                assert(results[1].length === 0);
                done();
            })
            .catch(done);
    });
});