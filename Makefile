PACKAGE_NAME=ctdb-ec2
PACKAGE_VERSION=1.2
PACKAGE_DIR=$(PACKAGE_NAME)-$(PACKAGE_VERSION)

all:
dist:
	rm -rvf $(PACKAGE_DIR)
	mkdir -vp $(PACKAGE_DIR)
	install -m 0755 interface_modify_ec2.sh $(PACKAGE_DIR)/interface_modify_ec2.sh
	install -m 0644 ec2.rc $(PACKAGE_DIR)/ec2.rc
	install -m 0644 ec2-eni-functions $(PACKAGE_DIR)/ec2-eni-functions
	install -m 0644 ec2-config $(PACKAGE_DIR)/ec2-config
	install -m 0644 Makefile $(PACKAGE_DIR)/Makefile
	install -m 0644 $(PACKAGE_NAME).spec $(PACKAGE_DIR)/$(PACKAGE_NAME).spec
	install -m 0644 README.md $(PACKAGE_DIR)/README.md
	install -m 0644 COPYING $(PACKAGE_DIR)/COPYING
	tar -cvf $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz $(PACKAGE_DIR)
rpm:
	make dist && rpmbuild -ta $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz

clean:
	rm -rvf $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz \
	$(PACKAGE_NAME)-$(PACKAGE_VERSION)
