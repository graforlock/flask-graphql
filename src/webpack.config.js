const webpack = require('webpack')
const path = require('path')

module.exports = {
  mode: 'development',
  context: __dirname,
  entry: "./index",
  output: {
    path: path.resolve(__dirname, "../static"),
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['@babel/preset-env']
        }
      }
    ]
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV)
    })
  ]
}