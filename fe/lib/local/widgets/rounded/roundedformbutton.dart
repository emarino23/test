import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';

class RoundedFormButton extends StatelessWidget {
  final double left;
  final double top;
  final double width;
  final double height;
  final double fontSize;
  final String label;
  final color;
  final Color textColor;
  final void Function()? onPressed;
  final fontWeight;

  const RoundedFormButton({
    Key? key,
    required this.label,
    this.left = 0,
    this.top = 0,
    this.width = 0.2,
    this.height = 0.05,
    this.fontSize = 8,
    this.color = Colors.black54,
    this.textColor = Colors.black54,
    this.fontWeight = FontWeight.normal,
    required this.onPressed,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextButton(
      style: ButtonStyle(
          shape: MaterialStateProperty.all<RoundedRectangleBorder>(
              RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(18.0),
                  side: BorderSide(color: Colors.grey)))),
      onPressed: onPressed,
      child: Text(
        label,
        textAlign: TextAlign.left,
        style: KTextSytle(
          context: context,
          fontSize: fontSize,
          fontWeight: FontWeight.bold,
          color: textColor,
        ).getStyle(),
      ),
    );
  }
}
