def remove_annotation(line: str) -> str:
    print(1)


if __name__ == '__main__':
    import xml.etree.ElementTree as ET

    # 定义JUnit 5的dependency XML结构
    junit5_dependency = """
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.2</version>
            <scope>test</scope>
        </dependency>
    """

    # 解析pom.xml
    # tree = ET.parse('E:/projects/java/jacoco_hello/pom.xml')
    tree = ET.parse('E:/projects/java/jacoco_hello/pom.xml')
    #
    root = tree.getroot()

    # 名称空间可能导致问题，尤其是在maven文件中，所以我们获取此文档的名称空间
    namespaces = {'m': 'http://maven.apache.org/POM/4.0.0'}
    ET.register_namespace('', namespaces['m'])

    # 检查是否存在 JUnit 依赖
    dependencies = root.find('m:dependencies', namespaces)
    has_junit5_dependency = False

    if dependencies is not None:
        for dependency in dependencies.findall('m:dependency', namespaces):
            groupId = dependency.find('m:groupId', namespaces).text
            artifactId = dependency.find('m:artifactId', namespaces).text

            if groupId == 'org.junit.jupiter' and artifactId.startswith('junit-jupiter'):
                has_junit5_dependency = True
                break

    # 如果不存在JUnit 5依赖，则加入依赖
    if not has_junit5_dependency:
        junit_dependency_xml = ET.fromstring(junit5_dependency)
        dependencies.append(junit_dependency_xml)
        tree.write('pom2.xml', encoding="utf-8", xml_declaration=True)
        print("JUnit 5 dependency added to pom2.xml.")
    else:
        print("JUnit 5 dependency already exists.")

