'use strict';

angular.module('myapp')
  .factory('User', ['$resource', function ($resource) {
    return $resource('myapp/users/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
