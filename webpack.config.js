const path = require("path");
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

var entry = ['./assets/entry.js'];

const output = {
  path: path.resolve('./static/dist'),
  filename: "[name]-[hash].js"
}

var plugins = [
    new MiniCssExtractPlugin({
        filename: '[name].[hash].css',
        chunkFilename: '[id].[hash].css'
    }),
    new webpack.ProvidePlugin({$: "jquery",jQuery: "jquery"}),
]

module.exports = {
  context: __dirname,
  entry: entry,
  output: output,
  plugins,
}
