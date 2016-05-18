module.exports = function(config) {
  config.set({
    basePath: '',
    frameworks: [
      'jasmine'
    ],
    files: [
      'temp/test/*.js'
    ],
    reporters: [
      'mocha'
    ],
    browsers: [
      'PhantomJS'
    ],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    singleRun: false
  });
};
