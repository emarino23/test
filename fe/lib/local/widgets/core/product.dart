import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../../../index.dart';

class ProductWidget extends StatelessWidget {
  const ProductWidget({Key? key, required this.product}) : super(key: key);
  final product;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(5),
      child: InkWell(
        onTap: () {
          showCustomDialog(context, HotelItineraryWidget(row: product), "Close",
              backgroundColor: Color.fromARGB(100, 0, 0, 0),
              buttonColor: Colors.white);
        },
        child: Container(
            width: Get.width * 0.2,
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(15.0),
                boxShadow: [
                  BoxShadow(
                      color: Colors.black.withOpacity(0.2),
                      spreadRadius: 3.0,
                      blurRadius: 5.0)
                ],
                color: Colors.white),
            child: Column(children: [
              Padding(
                  padding: EdgeInsets.all(5.0),
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [Text("")])),
              Hero(
                  tag: product["value"]["hotelname"] +
                      "_" +
                      product["value"]["roomcategory"],
                  child: Container(
                      height: Get.height * 0.25,
                      width: Get.width * 0.25,
                      decoration: BoxDecoration(
                          image: DecorationImage(
                              image: AssetImage(
                                  "assets/images/1x/Recurso_356mdpi.png"),
                              fit: BoxFit.contain)))),
              SizedBox(height: 7),
              Text(
                  product["value"]["hotelname"] +
                      "_" +
                      product["value"]["roomcategory"],
                  style: TextStyle(
                      color: Colors.black.withOpacity(0.2),
                      fontFamily: 'Varela',
                      fontSize: 14.0)),
              Padding(
                  padding: EdgeInsets.all(5.0),
                  child: Container(
                    color: Colors.green,
                    height: 1,
                  )),
              Padding(
                  padding: EdgeInsets.only(
                    left: 5,
                    right: 5,
                  ),
                  child: Row(children: [
                    ...[
                      CustomFormCounterFieldWidget(
                          initial: getFormValue(
                              globalctx.memory["destinations"],
                              globalDestinationIndex,
                              "hotelPax.${product["description"]}",
                              0),
                          min: 0,
                          max: 50,
                          step: 1,
                          original: true,
                          onValueChanged: (value) {
                            setFormValue(
                                globalctx.memory["destinations"],
                                globalDestinationIndex,
                                "hotelPax.${product["description"]}",
                                value);
                          },
                          label: 'Rooms',
                          width: 0.15),
                    ],
                  ]))
            ])),
      ),
    );
  }
}
