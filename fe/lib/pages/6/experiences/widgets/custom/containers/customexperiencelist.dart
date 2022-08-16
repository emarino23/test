import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'package:naver_crs/pages/6/experiences/widgets/custom/draggable/experiencedragtarget.dart';

class CustomExperiencesListWidget extends StatelessWidget {
  const CustomExperiencesListWidget({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: SizedBox(
          width: Get.width * 0.3,
          height: Get.height * 0.5,
          child: Column(
            children: [
              CustomTitleWidget(
                  fontWeight: FontWeight.bold,
                  label: "Suggested Experiences",
                  color: Colors.white),
              Scrollbar(
                child: SingleChildScrollView(
                    child: Column(children: experienceSelectedDragData.value)),
              ),
            ],
          )),
    );
  }
}
