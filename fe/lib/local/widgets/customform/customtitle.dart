import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../index.dart';
import 'index.dart';
import 'package:naver_crs/index.dart';

class CustomTitleWidget extends StatelessWidget {
  const CustomTitleWidget(
      {Key? key,
      required this.label,
      this.fontWeight = FontWeight.normal,
      this.width = 0.15,
      this.color = Colors.black,
      this.fontSize = 12})
      : super(key: key);
  final String label;
  final FontWeight fontWeight;
  final double width;
  final Color color;
  final fontSize;
  @override
  Widget build(BuildContext context) {
    return CustomFormLabelWidget(
        label: label, fontWeight: fontWeight, color: color, fontSize: fontSize);
  }
}
