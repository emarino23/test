import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../../index.dart';

// ignore: must_be_immutable
class RightWidget extends StatelessWidget {
  RightWidget({
    Key? key,
    required this.destination,
    required this.index,
    required this.ctrl,
    required this.formKey,
  }) : super(key: key);

  final destination;
  final index;
  final DestinationDetailController ctrl;
  GlobalKey<FormState> formKey;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(left: Get.width * 0.45, top: Get.height * 0.18),
      child: SizedBox(
        height: Get.height * 0.6,
        width: Get.width * 0.45,
        // color: Colors.red[50],
        child: SingleChildScrollView(
          child: CustomStarDestinationForm(
              destination: destination,
              index: index,
              ctrl: ctrl,
              formKey: formKey),
        ),
      ),
    );
  }
}
