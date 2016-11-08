var React = require('react');
var ReactDOM = require('react-dom');
var Hello = function () {
    return <h1>Hello, world!</h1>;
};

document.addEventListener('DOMContentLoaded', function () {
    ReactDOM.render(<Hello/>, document.getElementById("app"));
});