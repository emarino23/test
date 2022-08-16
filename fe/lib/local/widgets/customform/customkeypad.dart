import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';

class CustomKeypadWidget extends StatelessWidget {
  const CustomKeypadWidget({
    Key? key,
    required this.width,
    this.fontSize = 12,
    this.onNext,
    this.onPrevious,
    this.prevlabel = "< Previous",
    this.nextlabel = "Next >",
    this.nextFontWeight = FontWeight.normal,
    this.prevFontWeight = FontWeight.normal,
  }) : super(key: key);
  final fontSize;
  final double width;
  final String nextlabel;
  final String prevlabel;
  final FontWeight nextFontWeight;
  final FontWeight prevFontWeight;
  final onNext;
  final onPrevious;
  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        TextButton(
          onPressed: onPrevious,
          child: CustomFormLabelWidget(
              fontSize: fontSize, label: prevlabel, fontWeight: prevFontWeight),
        ),
        SizedBox(width: Get.width * width),
        TextButton(
          onPressed: onNext,
          child: CustomFormLabelWidget(
              fontSize: fontSize, label: nextlabel, fontWeight: nextFontWeight),
        ),
      ],
    );
  }
}
