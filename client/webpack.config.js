module.exports = {entry: "./index.js",
    output: {path: "../static", filename: "chess.js"},
    module: {
        loaders: [{ test: /\.js$/, exclude: /(node_modules)/, loader: 'babel-core'}]
    }
};