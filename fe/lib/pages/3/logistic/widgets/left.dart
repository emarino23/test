import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
import 'package:flutter_swiper/flutter_swiper.dart';

class LeftWidget extends StatelessWidget {
  const LeftWidget({
    Key? key,
    required this.images,
  }) : super(key: key);
  final images;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        top: Get.height * 0.01,
        left: Get.width * 0.05,
      ),
      child: SizedBox(
        height: Get.height * 0.9,
        width: Get.width * 0.4,
        child: Obx(() => Swiper(
              containerHeight: 100,
              containerWidth: 100,
              itemBuilder: (BuildContext context, int index) {
                return Image.asset("assets/images/" + images.value[index]);
              },
              autoplay: true,
              autoplayDelay: 5000,
              itemCount: images.value.length,
              scrollDirection: Axis.horizontal,
            )),
      ),
    );
  }
}
