import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';

class CustomDescriptionWidget extends StatelessWidget {
  const CustomDescriptionWidget({
    Key? key,
    this.text = '',
    this.width = 0.5,
    this.fontSize = 0.018,
    this.fontWeight = FontWeight.normal,
    this.textAlign = TextAlign.left,
  }) : super(key: key);

  final text;
  final width;
  final fontSize;
  final fontWeight;
  final textAlign;
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: Get.width * width,
      child: Text(text,
          textAlign: textAlign,
          style: GoogleFonts.poppins(
              textStyle: TextStyle(
            color: const Color.fromARGB(255, 0, 0, 0),
            fontSize: fontSize * 1.0,
            fontWeight: fontWeight,
          ))),
    );
  }
}
