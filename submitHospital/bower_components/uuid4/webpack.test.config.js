module.exports = {

  entry: './test/index.spec.js',

  output: {
    path: './temp/test/',
    filename: 'index.js'
  },

  module: {

    loaders: [
      {
        test: /\.js$/,
        loaders: ['babel-loader']
      }
    ]

  }

};
