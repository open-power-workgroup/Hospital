module.exports = {

  entry: './src/index.js',

  output: {
    path: './temp/lib/browser/',
    filename: 'index.js',
    library: 'UUID4',
    libraryTarget: 'umd'
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
