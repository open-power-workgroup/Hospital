'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.validate = validate;
exports.generate = generate;
var pattern = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx';

var replacements = {
  x: '0123456789abcdef',
  y: '89ab'
};

var pattern_re = /[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}/;

function getRandomCharacter(char_list) {
  var random_position = Math.floor(Math.random() * char_list.length);
  return char_list.charAt(random_position);
}

function getPatternCharacter(character) {
  return character in replacements ? getRandomCharacter(replacements[character]) : character;
}

function validate(id) {
  return pattern_re.test(id);
}

function generate() {
  return pattern.split('').map(getPatternCharacter).join('');
}