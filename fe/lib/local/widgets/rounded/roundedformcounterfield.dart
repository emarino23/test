import 'package:flutter/material.dart';
import 'package:counter/counter.dart';
import 'package:flutter_html/flutter_html.dart';
import 'package:get/get.dart';

import '../../index.dart';

class CounterConfig implements Configuration {
  var _fontSize = 12 * 1.0;

  var _backgroundColor = Color.fromARGB(0, 0, 0, 0);

  var _disableColor = Colors.grey;

  var _iconBorderRadius = 20.0;

  var _iconBorderWidth = 10.0;

  var _iconColor = Colors.black;

  var _size = Get.height * 0.1;

  var _textBackgroundColor = Color.fromARGB(0, 0, 0, 0);

  var _textColor = Colors.black;

  var _textWidth = Get.width * 0.05;

  var _iconStyle = IconStyle.add_minus_circle;

  @override
  get fontSize => _fontSize;

  set fontSize(double value) => _fontSize = value;
  CounterConfig({fontSize = 12 * 1.0}) {
    _fontSize = fontSize * 1.0;
  }

  @override
  Color? get textColor => Colors.black;

  @override
  Color? get textBackgroundColor => _textBackgroundColor;

  @override
  double get textWidth => 40;

  @override
  IconStyle get iconStyle => IconStyle.add_minus;

  @override
  Color? get iconColor => Colors.black87;

  @override
  Color? get disableColor => Colors.black12;

  @override
  Color? get backgroundColor => Colors.transparent;

  @override
  double? get iconBorderWidth => null;

  @override
  double? get iconBorderRadius => size / 2;

  @override
  // TODO: implement size
  double get size => 25;
}

class RoundedFormCounterField extends StatelessWidget {
  final bool disabled;
  final double left;
  final double top;
  final double width;
  final double height;
  final double fontSize;
  final String hintText;

  final void Function(num?)? onValueChanged;
  final int initial;
  final int min;
  final int max;
  final int bound;
  final int step;
  final bool original;

  RoundedFormCounterField(
      {Key? key,
      required this.hintText,
      this.left = 45,
      this.top = 5,
      this.width = 0.2,
      this.height = 0.06,
      this.fontSize = 0.1,
      this.onValueChanged,
      this.initial = 0,
      this.min = 0,
      this.max = 10,
      this.bound = 0,
      this.step = 1,
      this.disabled = false,
      this.original = false})
      : super(key: key);
  var config = CounterConfig(fontSize: 20);

  @override
  Widget build(BuildContext context) {
    var counter = Counter(
      configuration: config,
      initial: initial < min ? min : initial,
      min: initial > min ? min : initial,
      max: initial <= max ? max : initial,
      bound: bound < initial ? initial : bound,
      step: step,
      onValueChanged: onValueChanged ?? (value) {},
    );

    if (original) {
      counter = Counter(
        configuration: config,
        initial: initial,
        min: min,
        max: max,
        bound: bound,
        step: step,
        onValueChanged: onValueChanged ?? (value) {},
      );
    }

    return Container(
      width: Get.width * width,
      height: Get.height * height,
      padding: EdgeInsets.only(left: left, top: top),
      decoration: BoxDecoration(
          color: Colors.grey, borderRadius: BorderRadius.circular(50)),
      foregroundDecoration: BoxDecoration(
          color: Color.fromARGB(0, 0, 0, 0),
          borderRadius: BorderRadius.circular(50)),
      child: counter,
    );
  }
}
