import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:naver_crs/index.dart';
// ignore: import_of_legacy_library_into_null_safe
import 'package:flutter_swiper/flutter_swiper.dart';

class LeftGalleryWidget extends StatelessWidget {
  const LeftGalleryWidget({
    Key? key,
    required this.value,
    required this.catalog,
    required this.code,
  }) : super(key: key);
  final value;
  final catalog;
  final code;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        top: Get.height * 0.1,
        left: Get.width * 0.05,
      ),
      child: SizedBox(
          height: Get.height * 0.7,
          width: Get.width * 0.4,
          child: Obx(() {
            images = Rx(getCatalogValueByCode(catalog, code, "value", value));
            if (images.value != null && images.value.isNotEmpty) {
              return Swiper(
                containerHeight: 100,
                containerWidth: 100,
                itemBuilder: (BuildContext context, int index) {
                  return Image.asset("assets/images/" + images.value[index]);
                },
                autoplay: true,
                autoplayDelay: 10000,
                itemCount: images.value.length,
                scrollDirection: Axis.horizontal,
              );
            } else {
              return Padding(
                padding: EdgeInsets.only(
                  top: Get.height * 0.0,
                  left: Get.width * 0.1,
                ),
                child: Image.asset("assets/images/1x/logo.png"),
              );
            }
          })),
    );
  }
}
