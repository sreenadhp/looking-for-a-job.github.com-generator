var config = require('./webpack.config');

const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const autoprefixer = require('autoprefixer');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

const styleRule = {
  test: /\.(sa|sc|c)ss$/,
  use: [
    MiniCssExtractPlugin.loader,
    { loader: 'css-loader', options: { sourceMap: true } },
    { loader: 'postcss-loader', options: { plugins: () => [autoprefixer({ browsers: ['last 2 versions'] })] } },
    'sass-loader'
  ]
};

config.module = {rules: [styleRule]};

config.output.publicPath  = '/static/dist/'

config.plugins.unshift(new BundleTracker({filename: './webpack-stats.production.json'}));
config.plugins.concat([
    new CleanWebpackPlugin()
]);

config.optimization = {
  minimizer : [
    new UglifyJsPlugin({cache: true, parallel: true, sourceMap: true}),
    new OptimizeCSSAssetsPlugin({})
  ]
}
console.log(config.plugins)
module.exports = config
