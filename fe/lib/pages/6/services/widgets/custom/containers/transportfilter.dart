import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:get/get.dart';
import 'package:naver_crs/pages/6/services/widgets/custom/containers/leftHeader.dart';

// ignore: must_be_immutable
class DayExpFilter extends HookWidget {
  const DayExpFilter({Key? key, required this.ctrl, this.counter})
      : super(key: key);
  final ServicesController ctrl;
  final counter;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        top: Get.height * 0,
        left: Get.width * 0.6,
      ),
      child: BodyWidget(
        ctrl: ctrl,
        counter: counter,
      ),
    );
  }
}

// ignore: must_be_immutable
class BodyWidget extends StatelessWidget {
  const BodyWidget({
    Key? key,
    this.ctrl,
    this.counter,
  }) : super(key: key);
  final ctrl;
  final counter;
  @override
  Widget build(BuildContext context) {
    return Obx(() {
      var t = arrivalDate.value;
      return Form(
        key: formKey,
        child: Padding(
          padding: EdgeInsets.only(
            top: Get.height * 0.06,
            left: Get.width * 0.08,
          ),
          child: SizedBox(
              width: Get.width * 0.25,
              height: Get.height,
              child: Column(
                children: [
                  LeftHeader(ctrl: ctrl, counter: counter),
                ],
              )),
        ),
      );
    });
  }
}
