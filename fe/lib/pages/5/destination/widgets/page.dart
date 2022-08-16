import 'package:flutter/material.dart';
import 'index.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';

class DestinationWidget extends GetView<DestinationController> {
  const DestinationWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        CustomDestinationTitleWidget(),
        CustomLeftStarDestinationForm(),
        CustomRightStarDestinationForm(),
      ],
    );
  }
}
