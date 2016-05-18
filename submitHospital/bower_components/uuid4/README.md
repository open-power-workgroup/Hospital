# UUID4

Generator and validator for [Universally Unique Identifier v4 (random)](http://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29).

## How to use

```javascript
// generate unique ID, e.g. 1b7d6095-0cea-4426-9e3d-1608263df5fb
UUID4.generate();

// validate ID
UUID4.validate('xxx');  // -> false
UUID4.validate('1b7d6095-0cea-4426-9e3d-1608263df5fb');  // -> true

```

## Bug reports, feature requests and contact

If you found any bugs, if you have feature requests or any questions, please, either [file an issue at GitHub](https://github.com/fczbkk/uuid4/issues) or send me an e-mail at [riki@fczbkk.com](mailto:riki@fczbkk.com).

## License

UUID4 is published under the [MIT license](https://github.com/fczbkk/uuid4/blob/master/LICENSE). Feel free to use it in any way.
